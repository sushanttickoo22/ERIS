import { BrowserRouter, Routes, Route, Link } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Upload from "./pages/Upload";

export default function App() {

    return (

        <BrowserRouter>

            <nav
                style={{
                    display: "flex",
                    gap: "20px",
                    padding: "20px",
                    borderBottom: "1px solid #ccc"
                }}
            >

                <Link to="/">Dashboard</Link>

                <Link to="/upload">Upload</Link>

            </nav>

            <Routes>

                <Route
                    path="/"
                    element={<Dashboard />}
                />

                <Route
                    path="/upload"
                    element={<Upload />}
                />

            </Routes>

        </BrowserRouter>

    );

}
