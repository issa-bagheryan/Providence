from rich.table import Table


class Dashboard:
    def build(self, stats):
        table = Table(title="👁 Watching ")

        table.add_column("Metric", style="cyan")
        table.add_column("Value", style="bold green")

        table.add_row("🚗 Cars", str(stats["cars"]))
        table.add_row("🧍 People", str(stats["people"]))
        table.add_row("🚦 Traffic", stats["traffic"])

        alert = "🔴 HIGH" if stats["alert"] else "🟢 NORMAL"
        table.add_row("⚠ Alert", alert)

        return table