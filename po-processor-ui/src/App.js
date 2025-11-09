import React, { useState } from "react";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => setFile(e.target.files[0]);

  const handleSubmit = async () => {
    if (!file) return alert("Please upload a file first!");
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:5000/process", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setResult(data);
    setLoading(false);
  };

  return (
    <div style={{ maxWidth: 800, margin: "auto", fontFamily: "sans-serif" }}>
      <h2>PO Processing POC</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleSubmit} disabled={loading}>
        {loading ? "Processing..." : "Process"}
      </button>

      {result && (
        <div style={{ marginTop: 20 }}>
          {Object.entries(result).map(([stage, content]) => (
            <div key={stage} style={{ marginBottom: 10 }}>
              <h4>{stage.toUpperCase()}</h4>
              <pre
                style={{
                  background: "#f4f4f4",
                  padding: 10,
                  borderRadius: 8,
                  whiteSpace: "pre-wrap",
                }}
              >
                {content}
              </pre>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
