import axios from "axios";

const API_BASE = "http://127.0.0.1:8000/api";

export async function analyze(query) {
    const response = await axios.post(`${API_BASE}/analyze/`, { query });
    return response.data;
}

export async function downloadExcel(rows) {
    const response = await fetch(`${API_BASE}/download/`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ rows })
    });

    const blob = await response.blob();
    const url = window.URL.createObjectURL(blob);

    const a = document.createElement("a");
    a.href = url;
    a.download = "filtered_data.xlsx";
    a.click();
}
