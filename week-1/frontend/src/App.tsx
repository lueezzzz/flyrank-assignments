import { useEffect, useState } from "react";
import getTasks, { BASE_URL } from "./api/client";
import type { Task } from "./types";

function App() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [task, setTask] = useState("");
  const [id, setId] = useState<number>(0);
  const [specificTask, setSpecificTask] = useState<Task>();
  const [searchId, setSearchId] = useState<number>(0);
  const [editId, setEditId] = useState<number>(0);
  const [editTitle, setEditTitle] = useState<string>("");
  const [editIsDone, setEditIsDone] = useState<boolean>(false);

  async function handleAddTask() {
    const res = await fetch(`${BASE_URL}/tasks`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ title: task, done: false }),
    });

    if (res.ok) {
      const newTask = await res.json();

      setTasks([...tasks, newTask]);
      setTask("");
    }
  }

  async function handleRemoveTask(id: number) {
    const res = await fetch(`${BASE_URL}/tasks/${id}`, {
      method: "DELETE",
    });

    if (res.ok) {
      setTasks(tasks.filter((task) => task.id !== id));
    }
  }

  async function handleGetSpecificTask(id: number) {
    const res = await fetch(`${BASE_URL}/tasks/${id}`, {
      method: "GET",
      headers: { "Content-Type": "application/json" },
    });

    if (res.ok) {
      setSpecificTask(await res.json());
    }
  }

  async function handleEditTask(id: number, newTitle: string, isDone: boolean) {
    const res = await fetch(
      `${BASE_URL}/tasks/${id}?title=${newTitle}&done=${isDone}`,
      {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
      },
    );

    if (res.ok) {
      const updatedTask = await res.json();
      setTasks(tasks.map((task) => (task.id === id ? updatedTask : task)));
    }
  }

  useEffect(() => {
    getTasks()
      .then((data) => setTasks(data))
      .catch((err) => console.error(err));
  }, []);

  return (
    <>
      <div>
        <label>Add Task: </label>
        <input
          type="text"
          value={task}
          onChange={(e) => setTask(e.target.value)}
        />
        <button onClick={handleAddTask}>Add task</button>
      </div>

      <div>
        <label>Get Specific Task: </label>
        <input
          type="number"
          value={searchId}
          onChange={(e) => setSearchId(Number(e.target.value))}
        />
        <button onClick={() => handleGetSpecificTask(searchId)}>
          Get Task
        </button>
        {specificTask && (
          <div>
            Found: {specificTask.title} -{" "}
            {specificTask.done ? "Done" : "Not Done"}
          </div>
        )}
      </div>

      <div>
        <label>Remove Task: </label>
        <input
          type="number"
          value={id}
          onChange={(e) => setId(Number(e.target.value))}
        />
        <button onClick={() => handleRemoveTask(id)}>Remove Task</button>
      </div>

      <div>
        <label>Edit Task: </label>
        <input
          type="number"
          placeholder="Task ID"
          value={editId}
          onChange={(e) => setEditId(Number(e.target.value))}
        />
        <input
          type="text"
          placeholder="New Title"
          value={editTitle}
          onChange={(e) => setEditTitle(e.target.value)}
        />
        <label>
          Done:
          <input
            type="checkbox"
            checked={editIsDone}
            onChange={(e) => setEditIsDone(e.target.checked)}
            style={{ marginLeft: "5px", marginRight: "10px" }}
          />
        </label>
        <button onClick={() => handleEditTask(editId, editTitle, editIsDone)}>
          Update Task
        </button>
      </div>

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
    </>
  );
}

export default App;
