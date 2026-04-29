import { motion } from "framer-motion";

export default function ResultCard({ label, confidence }) {
return (
<motion.div
className="card"
initial={{ opacity: 0, y: 30 }}
animate={{ opacity: 1, y: 0 }}
> <h2>{label}</h2> <p>Confidence: {(confidence * 100).toFixed(2)}%</p>
</motion.div>
);
}
