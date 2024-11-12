// Home.jsx
import React, { useState, useEffect } from "react";
import NavBar from "./NavBar";
import Sidebar from "./Sidebar";
import WeeklySchedule from "./WeeklySchedule";
import EventModal from "./EventModal";

// Função auxiliar para obter o início da semana para uma data
const getWeekStart = (date) => {
  const day = new Date(date);
  const diff = day.getDate() - day.getDay() + (day.getDay() === 0 ? -6 : 1); // Ajusta para segunda-feira como início da semana
  return new Date(day.setDate(diff)).toDateString();
};

export default function Home() {
  const [selectedDate, setSelectedDate] = useState(new Date());
  const [eventsByDate, setEventsByDate] = useState({});
  const [currentEvents, setCurrentEvents] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentEvent, setCurrentEvent] = useState(null);

  useEffect(() => {
    // Atualiza os eventos da semana atual quando a data muda
    const weekStart = getWeekStart(selectedDate);
    setCurrentEvents(eventsByDate[weekStart] || []);
  }, [selectedDate, eventsByDate]);

  // Função para abrir o modal de edição/criação de evento
  const handleEventClick = (day, time) => {
    setCurrentEvent({ day, time });
    setIsModalOpen(true);
  };

  // Função para salvar um evento e organizar por semana
  const handleSaveEvent = (newEvent) => {
    const weekStart = getWeekStart(selectedDate);
    setEventsByDate((prevEventsByDate) => {
      const updatedWeekEvents = [...(prevEventsByDate[weekStart] || [])];
      // Remove eventos duplicados no mesmo horário e dia
      const filteredEvents = updatedWeekEvents.filter(
        (e) => !(e.day === newEvent.day && e.time === newEvent.time)
      );
      return {
        ...prevEventsByDate,
        [weekStart]: [...filteredEvents, newEvent],
      };
    });
    setIsModalOpen(false);
  };

  // Função para lidar com a mudança de data no calendário
  const handleDateChange = (date) => {
    const newWeekStart = getWeekStart(date);
    const currentWeekStart = getWeekStart(selectedDate);

    if (newWeekStart !== currentWeekStart) {
      // Muda para uma nova semana e atualiza os eventos da semana selecionada
      setCurrentEvents(eventsByDate[newWeekStart] || []);
    }
    setSelectedDate(date);
  };

  return (
    <>
      <div>
        <NavBar />
      </div>
      <div className="flex h-screen">
        <Sidebar onDateChange={handleDateChange} />
        <WeeklySchedule events={currentEvents} selectedDate={selectedDate} onEventClick={handleEventClick} />
        {isModalOpen && (
          <EventModal
            event={currentEvent}
            onClose={() => setIsModalOpen(false)}
            onSave={handleSaveEvent}
          />
        )}
      </div>
    </>
  );
}
