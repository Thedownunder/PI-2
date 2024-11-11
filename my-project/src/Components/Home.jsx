// Home.jsx
import React, { useState } from "react";
import NavBar from "./NavBar";
import Sidebar from "./Sidebar";
import WeeklySchedule from "./WeeklySchedule";
import EventModal from "./EventModal";

export default function Home() {
  const [selectedDate, setSelectedDate] = useState(new Date());
  const [events, setEvents] = useState([
    { day: "Segunda", time: "08:00", title: "Meeting", color: "#FF6347" },
    { day: "Terça", time: "09:00", title: "Workshop", color: "#1E90FF" },
    { day: "Quarta", time: "12:00", title: "Presentation", color: "#9370DB" },
    { day: "Quinta", time: "17:00", title: "Client Call", color: "#FFA500" },
    { day: "Sexta", time: "15:00", title: "Review", color: "#32CD32" },
  ]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentEvent, setCurrentEvent] = useState(null);

  // Função para abrir o modal
  const handleEventClick = (day, time) => {
    setCurrentEvent({ day, time });
    setIsModalOpen(true);
  };

  // Função para salvar o evento
  const handleSaveEvent = (newEvent) => {
    setEvents((prevEvents) => {
      // Remove eventos duplicados para o mesmo horário e dia
      const filteredEvents = prevEvents.filter(
        (e) => !(e.day === newEvent.day && e.time === newEvent.time)
      );
      return [...filteredEvents, newEvent];
    });
    setIsModalOpen(false);
  };

  return (
    <>
      <div>
        <NavBar />
      </div>
      <div className="flex h-screen">
        <Sidebar onDateChange={setSelectedDate} />
        <WeeklySchedule events={events} selectedDate={selectedDate} onEventClick={handleEventClick} />
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
