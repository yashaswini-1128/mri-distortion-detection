export default function About() {
  return (
    <div className="container">
      <h1>About Project</h1>

      <p>
        This project is an AI-powered MRI distortion detection system using
        deep learning and Grad-CAM visualization.
      </p>

      <ul>
        <li>Model: CNN (ResNet18)</li>
        <li>Explainability: Grad-CAM</li>
        <li>Backend: FastAPI</li>
        <li>Frontend: React</li>
      </ul>
    </div>
  );
}