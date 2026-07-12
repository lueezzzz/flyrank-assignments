import express from "express";
import type { Request, Response } from "express";
import cors from 'cors';
import userRoutes from './routes/users.js';


const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());


app.use("/users", userRoutes)


app.get("/health", (req: Request, res: Response) => {
  res.status(200).json({
    status: "healthy",
    message: "running"
  });
});

app.listen(PORT, () => {
  console.log(`listening on ${PORT}`);
});
