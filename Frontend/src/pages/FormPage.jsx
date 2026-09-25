import { useState } from "react";

import ResultModal from "../components/ResultModal";
import GrantApplicationForm from "../components/GrantApplicationForm";

import toast from "react-hot-toast";

export default function App() {
  const [result, setResult] = useState(null);
  const [showModal, setShowModal] = useState(false);

  const handleSubmit = async (formData) => {
    console.log("========== HANDLE SUBMIT START ==========");
    console.log("Form Data:", formData);

    const loadingToast = toast.loading("Waking up GrantGuard AI agent...");

    try {
      // ==========================================
      // 1. Get JWT token
      // ==========================================

      const token = localStorage.getItem("token");

      console.log("JWT Token:", token);

      if (!token) {
        toast.error("Please login first.", {
          id: loadingToast,
        });

        return;
      }

      // ==========================================
      // 2. Ping backend
      // ==========================================

      console.log("1. Pinging backend...");

      const pingResponse = await fetch("http://127.0.0.1:8000");

      console.log("Ping Status:", pingResponse.status);

      if (!pingResponse.ok) {
        throw new Error("Backend is not available");
      }

      toast.success("Agent is online. Starting evaluation...", {
        id: loadingToast,
      });

      // ==========================================
      // 3. Send evaluation request
      // ==========================================

      console.log("2. Sending evaluation request...");

      const response = await fetch("http://127.0.0.1:8000/evaluate", {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },

        body: JSON.stringify(formData),
      });

      console.log("Evaluation Response Status:", response.status);

      const data = await response.json();

      console.log("Evaluation Response:");
      console.log(data);

      // ==========================================
      // 4. Handle authentication errors
      // ==========================================

      if (response.status === 401) {
        localStorage.removeItem("token");

        toast.error("Session expired. Please login again.");

        return;
      }

      // ==========================================
      // 5. Handle other API errors
      // ==========================================

      if (!response.ok) {
        const errorMessage =
          data?.detail?.[0]?.msg || data?.detail || "Evaluation failed.";

        toast.error(
          typeof errorMessage === "string"
            ? errorMessage
            : "Evaluation failed.",
        );

        console.error("Evaluation error:", data);

        return;
      }

      // ==========================================
      // 6. Display result
      // ==========================================

      setResult(data);
      setShowModal(true);

      toast.success("Evaluation completed.");

      // ==========================================
      // 7. Prepare notification
      // ==========================================

      console.log("3. Preparing notification...");

      const decision = data?.final_decision;

      console.log("Decision Object:");
      console.log(decision);

      if (!decision) {
        console.warn("No final_decision returned from backend.");

        return;
      }

      const message = `
Decision: ${decision.decision}

Confidence: ${decision.confidence}%

Summary:
${decision.summary}

Reasons:
${
  Array.isArray(decision.reasons)
    ? decision.reasons.map((r) => `• ${r}`).join("\n")
    : "No reasons provided."
}
`;

      console.log("Notification Message:");
      console.log(message);
    } catch (err) {
      console.error("========== ERROR ==========");
      console.error(err);

      toast.error("Unable to connect to GrantGuard.", {
        id: loadingToast,
      });
    }
  };

  return (
    <>
      <GrantApplicationForm onSubmit={handleSubmit} />

      <ResultModal
        open={showModal}
        result={result}
        onClose={() => setShowModal(false)}
      />
    </>
  );
}
