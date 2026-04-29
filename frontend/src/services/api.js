export async function predictImage(file) {
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://127.0.0.1:8000/api/v1/predict", {
        method: "POST",
        body: formData
    });

    if (!res.ok) {
        throw new Error("API Error");
    }

    return await res.json();
}