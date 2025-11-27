import React, { useState, useRef, useEffect } from "react";
import ChatInput from "./components/ChatInput";
import TrendChart from "./components/TrendChart";
import DataTable from "./components/DataTable";
import { analyze, downloadExcel } from "./api";   // <-- UPDATED: added downloadExcel

export default function App() {
  const [messages, setMessages] = useState([
    { id: 1, role: "assistant", text: "Hi — ask me about Pune areas, eg. 'Analyze Wakad' or 'Compare Baner and Aundh'." }
  ]);

  const [loading, setLoading] = useState(false);
  const winRef = useRef(null);

  // Auto-scroll on message update
  useEffect(() => {
    if (winRef.current) {
      winRef.current.scrollTop = winRef.current.scrollHeight + 200;
    }
  }, [messages, loading]);

  async function handleSend(query) {
    if (!query) return;

    // Add user message
    const userMsg = { id: Date.now(), role: "user", text: query };
    setMessages(prev => [...prev, userMsg]);
    setLoading(true);

    try {
      const res = await analyze(query);

      const assistantMsg = {
        id: Date.now() + 1,
        role: "assistant",
        text: res.summary,
        trend: res.trend,
        table: res.table
      };

      setMessages(prev => [...prev, assistantMsg]);

    } catch (err) {
      setMessages(prev => [...prev, {
        id: Date.now() + 2,
        role: "assistant",
        text: "Server error. Try again."
      }]);
    }

    setLoading(false);
  }

  return (
    <div className="app-wrap">
      <div className="chat-col" aria-label="Chat Window">

        {/* Header */}
        <div className="chat-header">
          <h2>Real Estate Analysis Dashboard</h2>
          <p>Try: <i>"Analyze Wakad"</i> • <i>"Compare Baner and Aundh"</i></p>
        </div>

        {/* Messages */}
        <div className="chat-window" ref={winRef}>
          {messages.map(m => (
            <div key={m.id} className={`msg ${m.role === "user" ? "user" : "assistant"}`}>

              {/* User message */}
              {m.role === "user" ? (
                <div className="summary-pre">{m.text}</div>
              ) : (
                <>
                  {/* Assistant summary */}
                  <div className="summary-pre">{m.text}</div>

                  {/* Single-area trend */}
                  {m.trend && Array.isArray(m.trend) && (
                    <div className="card-inside">
                      <div className="chart">
                        <TrendChart data={m.trend} />
                      </div>

                      {/* DOWNLOAD BUTTON */}
                      {m.table && (
                        <button
                          className="download-btn"
                          onClick={() => downloadExcel(m.text)}
                        >
                          Download Excel
                        </button>
                      )}

                      <div style={{ marginTop: 12 }}>
                        <DataTable rows={m.table} />
                      </div>
                    </div>
                  )}

                  {/* MULTI-AREA TREND */}
                  {m.trend && typeof m.trend === "object" && !Array.isArray(m.trend) && (
                    <div className="card-inside">

                      {Object.keys(m.trend).map(area => (
                        <div key={area} style={{ marginBottom: 14 }}>
                          <h5 style={{ margin: 0, color: "#fff" }}>{area}</h5>
                          <TrendChart data={m.trend[area]} />
                        </div>
                      ))}

                      {/* DOWNLOAD BUTTON */}
                      {m.table && (
                        <button
                          className="download-btn"
                          onClick={() => downloadExcel(m.table)}
                        >
                          Download Excel
                        </button>
                      )}

                      <div style={{ marginTop: 12 }}>
                        <DataTable rows={m.table} />
                      </div>

                    </div>
                  )}
                </>
              )}

            </div>
          ))}

          {loading && (
            <div className="msg assistant">
              <div className="summary-pre">Analyzing...</div>
            </div>
          )}
        </div>

        {/* Input */}
        <div className="chat-input-wrapper">
          <div className="input-bar">
            <ChatInput onSend={handleSend} />
          </div>
        </div>

      </div>
    </div>
  );
}
