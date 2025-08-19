def generate_report(anomaly_counts, cluster_results):
    """Markdown raporu oluşturur."""
    lines = ["# Su Kalitesi Analizi Raporu\n"]
    lines.append("## Anomali Tespiti")
    for method, count in anomaly_counts.items():
        lines.append(f"- {method}: {count} anomali")
    lines.append("\n## Kümeleme")
    for method, res in cluster_results.items():
        lines.append(f"- {method}: {res}")
    with open("water_quality_report.md", "w") as f:
        f.write("\n".join(lines))
