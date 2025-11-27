import React from 'react';

export default function ResponseCard({ summary }) {
    return (
        <div className="card">
            <h4 style={{ marginBottom: "10px", color: "#fff" }}>Summary</h4>
            <pre style={{ whiteSpace: "pre-wrap", color: "#ddd" }}>
                {summary}
            </pre>
        </div>
    );
}
