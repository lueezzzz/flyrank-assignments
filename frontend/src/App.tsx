import { useEffect, useState } from "react";
import getTasks from "./api/client";
import type { Task } from "./types";

function App() {
  const [tasks, setTasks] = useState<Task[]>([]);

  useEffect(() => {
    getTasks()
      .then((data) => setTasks(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <div>
      <h1>My Tasks</h1>
      <ul>
        {tasks.map((task) => (
          <li key={task.id}>
            {task.title} {task.done ? "(Done)" : ""}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
