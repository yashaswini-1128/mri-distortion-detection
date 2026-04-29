export default function ImagePreview({ src }) {
  if (!src) return null;

  return (
    <div style={{ marginTop: 15 }}>
      <h4>Preview</h4>
      <img
        src={src}
        alt="preview"
        style={{
          width: "250px",
          borderRadius: "10px",
          border: "1px solid #1e293b"
        }}
      />
    </div>
  );
}