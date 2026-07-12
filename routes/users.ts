import { Router} from "express";
import type {Request, Response } from "express";

const router = Router()

router.get('/', (req: Request, res: Response) => {
    res.json({
        message: "users",
    })
});

router.post('/', (req: Request, res: Response )=> {
    res.json({
        message: "user created"
    })
});


export default router