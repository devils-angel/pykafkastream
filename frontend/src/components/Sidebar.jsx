import { Link } from "react-router-dom";

export default function Sidebar() {
  return (
    <div className="w-64 bg-sidebar flex flex-col p-6 space-y-6 shadow-lg">
      <h2 className="text-xl font-bold text-accent">📊 MyApp</h2>
      <nav className="flex flex-col gap-4">
        <Link to="/dashboard" className="hover:text-accent">Dashboard</Link>
        <Link to="/login" className="hover:text-accent">Logout</Link>
      </nav>
    </div>
  );
}
