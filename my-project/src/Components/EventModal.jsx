// EventModal.jsx
import React, { useState } from "react";
import "./EventModal.css";

export default function EventModal({ event, onClose, onSave }) {
  const [title, setTitle] = useState(event?.title || "");
  const [color, setColor] = useState(event?.color || "#FF6347");

  const handleSubmit = () => {
    onSave({ ...event, title, color });
  };

  return (
    <div className="modal-overlay">
      <div className="modal">
        <h2>{event.title ? "Editar Evento" : "Adicionar Evento"}</h2>
        <input
          type="text"
          placeholder="Título do Evento"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
        <input
          type="color"
          value={color}
          onChange={(e) => setColor(e.target.value)}
        />
        <button onClick={handleSubmit}>Salvar</button>
        <button onClick={onClose}>Cancelar</button>
      </div>
    </div>
  );
}
