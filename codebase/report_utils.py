def generate_report(transcript):
    """Create simple text report"""
    lines = []
    for line in transcript:
        speaker = line.get("speaker", "Unknown")
        text = line.get("text", "")
        analysis = line.get("analysis", {})
        lines.append(f"{speaker}: {text}")
        if speaker.lower() == "customer" and analysis:
            lines.append(f"  Sentiment: {analysis.get('sentiment')}")
            lines.append(f"  Intent: {analysis.get('intent')}")
            lines.append(f"  Entities: {analysis.get('entities')}")
            lines.append(f"  Next Questions: {analysis.get('next_question')}")
            lines.append(f"  Objection Handling: {analysis.get('objection_handling')}")
            lines.append(f"  Product Recommendation: {analysis.get('product_recommendation')}")
            lines.append(f"  Auto Reply: {analysis.get('auto_reply')}")
    report_path = "call_report.txt"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    return report_path
