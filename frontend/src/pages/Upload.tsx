import { useState } from "react";

import {
    Alert,
    Box,
    Button,
    Card,
    CardContent,
    LinearProgress,
    Stack,
    Typography,
} from "@mui/material";

import CloudUploadIcon from "@mui/icons-material/CloudUpload";

import api from "../services/api";
import { UploadResponse } from "../types/upload";

export default function Upload() {

    const [selectedFile, setSelectedFile] = useState<File | null>(null);

    const [progress, setProgress] = useState(0);

    const [uploading, setUploading] = useState(false);

    const [response, setResponse] = useState<UploadResponse | null>(null);

    const selectFile = (
        e: React.ChangeEvent<HTMLInputElement>
    ) => {

        if (!e.target.files?.length) return;

        const file = e.target.files[0];

        if (!file.name.toLowerCase().endsWith(".pdf")) {

            alert("Please select a PDF.");

            return;

        }

        setSelectedFile(file);

    };

    async function upload() {

        if (!selectedFile) return;

        setUploading(true);

        const formData = new FormData();

        formData.append(
            "file",
            selectedFile
        );

        const result = await api.post<UploadResponse>(
            "/upload/",
            formData,
            {
                headers: {
                    "Content-Type": "multipart/form-data"
                },

                onUploadProgress(progressEvent) {

                    if (!progressEvent.total) return;

                    setProgress(
                        Math.round(
                            (progressEvent.loaded * 100) /
                                progressEvent.total
                        )
                    );

                }
            }
        );

        setResponse(result.data);

        setUploading(false);

    }

    return (

        <Box maxWidth={700}>

            <Typography
                variant="h4"
                gutterBottom
            >
                Upload Electoral Roll
            </Typography>

            <Card>

                <CardContent>

                    <Stack spacing={3}>

                        <Button
                            component="label"
                            variant="contained"
                            startIcon={<CloudUploadIcon />}
                        >
                            Browse PDF

                            <input
                                hidden
                                type="file"
                                accept=".pdf"
                                onChange={selectFile}
                            />

                        </Button>

                        {selectedFile && (

                            <Alert severity="info">

                                <strong>{selectedFile.name}</strong>

                                <br />

                                Size :

                                {" "}

                                {(
                                    selectedFile.size /
                                    1024 /
                                    1024
                                ).toFixed(2)}

                                MB

                            </Alert>

                        )}

                        {uploading && (

                            <LinearProgress
                                variant="determinate"
                                value={progress}
                            />

                        )}

                        <Button
                            variant="contained"
                            disabled={
                                !selectedFile ||
                                uploading
                            }
                            onClick={upload}
                        >

                            Upload

                        </Button>

                        {response && (

                            <Alert severity="success">

                                File uploaded successfully.

                                <br />

                                File ID :
                                {" "}
                                {response.file_id}

                            </Alert>

                        )}

                    </Stack>

                </CardContent>

            </Card>

        </Box>

    );

}
