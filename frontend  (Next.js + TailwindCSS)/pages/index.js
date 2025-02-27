import UploadForm from "../components/UploadForm";
import EnrollmentList from "../components/EnrollmentList";
import Predictions from "../components/Predictions";
import Card from "../components/Card";

export default function Home() {
  return (
    <div className="container mx-auto p-6">
      <h1 className="text-3xl font-bold text-center mb-6">🌟 Childcare Management Dashboard 🌟</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card title="📂 Upload Child Data">
          <UploadForm />
        </Card>

        <Card title="📝 Enrollments">
          <EnrollmentList />
        </Card>

        <Card title="📊 Future Predictions">
          <Predictions />
        </Card>
      </div>
    </div>
  );
}