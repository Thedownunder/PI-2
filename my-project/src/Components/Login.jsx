import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import InputLogin from "./InputLogin";
import "./Login.css";

export default function Login() {
    const navigate = useNavigate();
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const handleLogin = (event) => {
        event.preventDefault(); // Previne o envio padrão do formulário
        // Lógica de autenticação simulada
        if (username === "admin" && password === "password") {
            // Se as credenciais estiverem corretas, redireciona para a Home
            navigate("/home");
        } else {
            // Caso contrário, exibe uma mensagem de erro
            setError("Credenciais inválidas. Tente novamente.");
        }
    };

    return (
        <>
            <div className="flex">
                <div className="left_login w-screen h-screen">
                    <div className="paw-container">
                        {/* Ícones de patinhas */}
                        {[...Array(10)].map((_, i) => (
                            <img
                                key={i}
                                src="https://cdn-icons-png.flaticon.com/512/12/12638.png"
                                className="paw mx-auto h-20 w-auto"
                                alt="Paw print"
                            />
                        ))}
                    </div>
                </div>
                <div className="w-screen h-screen flex   justify-center">
                    <div className="login-form">
                        <InputLogin
                            username={username}
                            setUsername={setUsername}
                            password={password}
                            setPassword={setPassword}
                            handleLogin={handleLogin}
                        />
                        {error && <p className="text-red-500 mt-2">{error}</p>}
                    </div>
                </div>
            </div>
        </>
    );
}
