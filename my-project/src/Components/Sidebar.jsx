// Sidebar.jsx
import React, { useState } from "react";
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import './Sidebar.css';

export default function Sidebar({ onDateChange }) {
  const [startDate, setStartDate] = useState(new Date()); // Estado para armazenar a data selecionada 

  const handleDateChange = (date) => {
    setStartDate(date);
    onDateChange(date); // Envia a data selecionada para o componente pai (Home)
  };

  return (
    <div className="w-64 h-screen bg-orange-900 text-white p-4 flex flex-col items-center">
      <h2 className="text-lg font-semibold mb-4">Calendário</h2>
      <DatePicker
        selected={startDate}
        onChange={handleDateChange} // Atualiza a data no calendário e no componente pai
        inline // Mostra o calendário aberto e visível
        dateFormat="dd/MM/yyyy"
      />
    </div>
  );
}
