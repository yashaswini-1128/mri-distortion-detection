import { useState } from "react";

export default function UploadBox({ onUpload }) {
  const [preview, setPreview] = useState(null);

  const handleChange = (e) => {
    const file = e.target.files[0];
    if (!file) return;

    setPreview(URL.createObjectURL(file));
    onUpload(file);
  };

  return (
    <div className="card" style={{ textAlign: "center" }}>
      <h3>Upload MRI Image</h3>

      <input type="file" accept="image/*" onChange={handleChange} />

      {preview && (
        <div style={{ marginTop: 15 }}>
          <img src={preview} width="250" style={{ borderRadius: 10 }} />
        </div>
      )}
    </div>
  );
}