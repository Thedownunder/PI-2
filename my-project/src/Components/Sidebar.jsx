import React, { useState } from "react";
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import './Sidebar.css'

export default function Sidebar() {
  const [startDate, setStartDate] = useState(new Date()); // Estado para armazenar a data selecionada 

  return (
    <div className="w-64 h-screen bg-orange-900 text-white p-4 fixed flex flex-col items-center">
      <h2 className="text-lg font-semibold mb-4">Calendário</h2>
      <DatePicker
        selected={startDate}
        onChange={(date) => setStartDate(date)}
        inline // Mostra o calendário aberto e visível
        dateFormat="dd/MM/yyyy"
        className="bg-orange-700 rounded-lg p-2"
      />
    </div>
  );
}
