import { Router} from "express";
import type {Request, Response } from "express";
import { pool } from "../db.js";

const router = Router()

router.get('/', async (req: Request, res: Response) => {
    try {
        const users = await pool.query('SELECT * FROM users');
        res.json(users.rows);
    } catch (error) {
        console.error(error);
        res.status(500).json({error: "failed fetching users"})
    }
});

router.post('/', async (req: Request, res: Response )=> {
    try {
        const {name, email} = req.body;
        if (!name || !email){
            res.status(400).json({error: "name + email required"});
            return;
        }

        const query = 'INSERT INTO users (name,email) VALUES ($1, $2) RETURNING *';
        const queryRes = await pool.query(query, [name, email]);

        res.status(201).json({
            message: "user created",
            user: queryRes.rows[0]
        })

    } catch (error) {
        console.error(error);
        res.status(500).json({error: "failed creating user"})
    }
});


export default router