import { useEffect, useState } from "react";

function App() {
  const [campaigns, setCampaigns] = useState([]);
  const [filter, setFilter] = useState("All");

  useEffect(() => {
    fetch("https://grippicamapigndashboard-production.up.railway.app/campaigns")
      .then((res) => res.json())
      .then((data) => setCampaigns(data))
      .catch((err) => console.log("API Error:", err));
  }, []);

  const filteredData =
    filter === "All" ? campaigns : campaigns.filter((c) => c.status === filter);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold text-center mb-6">
        Campaign Analytics Dashboard
      </h1>

      <div className="flex justify-center mb-4">
        <select
          className="p-2 border rounded shadow"
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
        >
          <option>All</option>
          <option>Active</option>
          <option>Paused</option>
        </select>
      </div>

      <div className="overflow-x-auto">
        <table className="w-full bg-white shadow-md rounded">
          <thead className="bg-blue-600 text-white">
            <tr>
              <th className="p-3">Campaign Name</th>
              <th>Status</th>
              <th>Clicks</th>
              <th>Cost ($)</th>
              <th>Impressions</th>
            </tr>
          </thead>

          <tbody>
            {filteredData.map((c) => (
              <tr key={c.id} className="text-center border-b hover:bg-gray-100">
                <td className="p-2">{c.name}</td>
                <td>{c.status}</td>
                <td>{c.clicks}</td>
                <td>{c.cost}</td>
                <td>{c.impressions}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default App;
