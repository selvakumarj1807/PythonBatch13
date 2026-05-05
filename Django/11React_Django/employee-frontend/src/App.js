import React, { useState } from "react";
import EmployeeList from "./components/EmployeeList";
import EmployeeForm from "./components/EmployeeForm";

function App() {
  const [selected, setSelected] = useState(null);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Employee CRUD App</h1>

      <EmployeeForm
        selected={selected}
        refresh={() => window.location.reload()}
      />

      <EmployeeList onEdit={(emp) => setSelected(emp)} />
    </div>
  );
}

export default App;