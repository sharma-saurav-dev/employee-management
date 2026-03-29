import { useEffect, useState } from 'react'

const API_URL = 'http://localhost:8000/employees'

function App() {
  const [employees, setEmployees] = useState([])
  const [form, setForm] = useState({
    first_name: '',
    last_name: '',
    email: '',
    position: '',
    salary: ''
  })
  const [editingId, setEditingId] = useState(null)

  const loadEmployees = async () => {
    const res = await fetch(API_URL)
    const data = await res.json()
    setEmployees(data)
  }

  useEffect(() => {
    loadEmployees()
  }, [])

  const clearForm = () => {
    setForm({ first_name: '', last_name: '', email: '', position: '', salary: '' })
    setEditingId(null)
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    const payload = { ...form, salary: Number(form.salary) }

    if (editingId) {
      await fetch(`${API_URL}/${editingId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      })
    } else {
      await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload),
      })
    }

    clearForm()
    loadEmployees()
  }

  const startEdit = (item) => {
    setEditingId(item.id)
    setForm({
      first_name: item.first_name,
      last_name: item.last_name,
      email: item.email,
      position: item.position,
      salary: item.salary,
    })
  }

  const deleteEmployee = async (id) => {
    await fetch(`${API_URL}/${id}`, { method: 'DELETE' })
    if (editingId === id) clearForm()
    loadEmployees()
  }

  return (
    <div className="app">
      <h1>Employee Management</h1>

      <form onSubmit={handleSubmit} className="employee-form">
        <h2>{editingId ? 'Edit' : 'Add'} Employee</h2>

        <input value={form.first_name} onChange={(e) => setForm({ ...form, first_name: e.target.value })} placeholder="First Name" required />
        <input value={form.last_name} onChange={(e) => setForm({ ...form, last_name: e.target.value })} placeholder="Last Name" required />
        <input value={form.email} onChange={(e) => setForm({ ...form, email: e.target.value })} placeholder="Email" type="email" required />
        <input value={form.position} onChange={(e) => setForm({ ...form, position: e.target.value })} placeholder="Position" required />
        <input value={form.salary} onChange={(e) => setForm({ ...form, salary: e.target.value })} placeholder="Salary" type="number" step="0.01" required />

        <div className="buttons">
          <button type="submit">{editingId ? 'Update' : 'Create'}</button>
          {editingId && <button type="button" onClick={clearForm}>Cancel</button>}
        </div>
      </form>

      <table className="employees-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Position</th>
            <th>Salary</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {employees.map((item) => (
            <tr key={item.id}>
              <td>{item.id}</td>
              <td>{item.first_name} {item.last_name}</td>
              <td>{item.email}</td>
              <td>{item.position}</td>
              <td>{item.salary.toFixed(2)}</td>
              <td>
                <button onClick={() => startEdit(item)}>Edit</button>
                <button onClick={() => deleteEmployee(item.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default App
