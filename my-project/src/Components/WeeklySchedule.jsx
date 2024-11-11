// WeeklySchedule.jsx
import React from "react";
import './WeeklySchedule.css';

export default function WeeklySchedule({ events, onEventClick }) {
  const daysOfWeek = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"];
  const timeSlots = [
    "08:00", "09:00", "10:00", "11:00", "12:00",
    "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"
  ];

  return (
    <div className="weekly-schedule w-screen">
      <div className="header">
        <div className="header-item"></div>
        {daysOfWeek.map((day, index) => (
          <div key={index} className="header-item">{day}</div>
        ))}
      </div>
      {timeSlots.map((time, rowIndex) => (
        <div key={rowIndex} className="time-row">
          <div className="time-cell">{time}</div>
          {daysOfWeek.map((day, colIndex) => {
            const event = events.find((e) => e.day === day && e.time === time);
            return (
              <div
                key={colIndex}
                className={`event-cell ${event ? "occupied" : ""}`}
                style={{ backgroundColor: event ? event.color : "transparent" }}
                onClick={() => onEventClick(day, time)} // Abre o modal
              >
                {event && event.title}
              </div>
            );
          })}
        </div>
      ))}
    </div>
  );
}
