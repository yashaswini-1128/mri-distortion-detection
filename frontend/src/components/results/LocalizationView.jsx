export default function LocalizationView({ image }) {
  return (
    <div className="card">
      <h3>Localization</h3>

      {image ? (
        <img src={image} style={{ width: "100%", borderRadius: 10 }} />
      ) : (
        <p>No image</p>
      )}
    </div>
  );
}