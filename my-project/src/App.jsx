import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Login from "./Components/Login";
import Home from "./Components/Home";
import CadastroCliente from "./Components/CadastroCliente";

function App() {
  return (
    <Router>
      <main>
        <Routes>
          {/* Rota para a tela de login */}
          <Route path="/" element={<Login />} />
          {/* Rota para a tela home */}
          <Route path="/home" element={<Home />} />
          {/* Rota para tela de Cadastro do Cliente */}
          <Route path="/cadastro-cliente" element={<CadastroCliente />} />
        </Routes>
      </main>
    </Router>
  );
}

export default App;
