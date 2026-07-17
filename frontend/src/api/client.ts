import type { Task } from "../types";

export const BASE_URL = "http://localhost:8000"

export default async function getTasks(): Promise<Task[]> {
  const res = await fetch(`${BASE_URL}/tasks`);
  if (!res.ok) throw new Error("failed to fetch task");
  return res.json();
}
