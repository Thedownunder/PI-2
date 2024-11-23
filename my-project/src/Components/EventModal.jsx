// EventModal.jsx
import React, { useState } from "react";
import "./EventModal.css";
import InputMask from 'react-input-mask';

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
        <div className="mt-2 mb-2">
          <label htmlFor="situacao" className="block text-sm/6 font-medium text-gray-900">Situação</label>
          <select id="situacao" name="situacao" autoComplete="situacao" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm">
            <option>Pendente</option>
            <option>Finalizado</option>
          </select>
        </div>

        <div className="mt-2 mb-2">
          <label htmlFor="servico" className=" block text-sm/6 font-medium text-gray-900">Serviço</label>
          <input type="text" name="servico" id="servico" autoComplete="servico" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" />
        </div>

        <div className="mt-2 mb-2">
          <label htmlFor="categoria" className=" block text-sm/6 font-medium text-gray-900">Categoria</label>
          <input type="text" name="categoria" id="categoria" autoComplete="categoria" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" />
        </div>

        <div className="mt-2 mb-2">
          <label htmlFor="cliente" className="block text-sm/6 font-medium text-gray-900">Cliente</label>
          <select id="cliente" name="cliente" autoComplete="cliente" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm">
            <option>------------</option>
            {/* <option>Finalizado</option> */}
          </select>
        </div>

        <div className="mt-2 mb-2">
          <label htmlFor="animal" className="block text-sm/6 font-medium text-gray-900">Animal</label>
          <select id="animal" name="animal" autoComplete="animal" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm">
            <option>-------------</option>
            {/* <option>Finalizado</option> */}
          </select>
        </div>

        <div className="mt-2 mb-2">
          <label htmlFor="observacao" className=" block text-sm/6 font-medium text-gray-900">Observação</label>
          <input type="text" name="observacao" id="observacao" autoComplete="observacao" className="block w-full rounded-md border border-gray-300 py-1.5 text-gray-900 placeholder:text-gray-400 focus:ring-orange-600 focus:outline-none focus:ring-2 sm:text-sm" />
        </div>

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
