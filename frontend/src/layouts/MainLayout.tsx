import { ReactNode } from "react";
import {
    AppBar,
    Box,
    Drawer,
    List,
    ListItemButton,
    ListItemText,
    Toolbar,
    Typography,
} from "@mui/material";
import { Link } from "react-router-dom";

const drawerWidth = 240;

interface Props {
    children: ReactNode;
}

const menu = [
    { text: "Dashboard", path: "/" },
    { text: "Upload", path: "/upload" },
    { text: "Compare", path: "/compare" },
    { text: "Reports", path: "/reports" },
    { text: "Settings", path: "/settings" },
];

export default function MainLayout({ children }: Props) {
    return (
        <Box sx={{ display: "flex" }}>
            <AppBar position="fixed">
                <Toolbar>
                    <Typography variant="h6">
                        ERIS - Election Roll Intelligence System
                    </Typography>
                </Toolbar>
            </AppBar>

            <Drawer
                variant="permanent"
                sx={{
                    width: drawerWidth,
                    "& .MuiDrawer-paper": {
                        width: drawerWidth,
                    },
                }}
            >
                <Toolbar />

                <List>
                    {menu.map((item) => (
                        <ListItemButton
                            key={item.text}
                            component={Link}
                            to={item.path}
                        >
                            <ListItemText primary={item.text} />
                        </ListItemButton>
                    ))}
                </List>
            </Drawer>

            <Box
                component="main"
                sx={{
                    flexGrow: 1,
                    p: 3,
                    ml: `${drawerWidth}px`,
                }}
            >
                <Toolbar />
                {children}
            </Box>
        </Box>
    );
}
