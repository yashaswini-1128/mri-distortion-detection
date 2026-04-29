import Navbar from "../components/layout/Navbar";
import UploadBox from "../components/upload/UploadBox";
import ResultCard from "../components/results/ResultCard";
import GradCamView from "../components/results/GradCamView";
import LocalizationView from "../components/results/LocalizationView";
import ChartView from "../components/results/ChartView";
import Loader from "../components/ui/Loader";
import usePredict from "../hooks/usePredict";

export default function Home() {
  const { predict, loading, result } = usePredict();

  return (
    <>
      <Navbar />

      <div className="container">

        {/* Upload */}
        <UploadBox onUpload={predict} />

        {/* Loader */}
        {loading && <Loader />}

        {/* Results */}
        {result && (
          <>
            <div className="grid">
              <ResultCard label={result.label} confidence={result.confidence} />
              <ChartView confidence={result.confidence} />
            </div>

            <div className="grid">
              <GradCamView image={result.gradcam} />
              <LocalizationView image={result.localized} />
            </div>
          </>
        )}

      </div>
    </>
  );
}