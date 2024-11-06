import React from "react";
import NavBar from "./NavBar";
import Sidebar from "./Sidebar";

export default function Home() {
    return(
        <>
        <div className="w-screen">
            <NavBar />
        </div>
        <div className="flex w-screen h-screen">
            <Sidebar />
        </div>
        </>
    )
}