import { BarChart, Bar, XAxis, Tooltip } from "recharts";

export default function ChartView({ confidence }) {
const data = [
{ name: "Confidence", value: confidence * 100 }
];

return ( <div className="card"> <h3>Confidence Chart</h3>

```
  <BarChart width={300} height={200} data={data}>
    <XAxis dataKey="name" />
    <Tooltip />
    <Bar dataKey="value" />
  </BarChart>
</div>


);
}
