try:
    from rich.console import Console
    from rich.panel import Panel

    console = Console()
    RICH_AVAILABLE = True
except ImportError:
    console = None
    RICH_AVAILABLE = False


def ui_print(text="", style=None):
    if RICH_AVAILABLE:
        if style:
            console.print(text, style=style)
        else:
            console.print(text)
    else:
        print(text)


def ui_header(title):
    if RICH_AVAILABLE:
        console.print(Panel.fit(f"[bold]{title}[/bold]", border_style="cyan"))
    else:
        print("\n" + "=" * 46)
        print(title)
        print("=" * 46)


def ui_section(title):
    if RICH_AVAILABLE:
        console.print(f"\n[bold cyan]{title}[/bold cyan]")
    else:
        print("\n" + title)


def ui_separator():
    if RICH_AVAILABLE:
        console.print("[dim]" + "-" * 46 + "[/dim]")
    else:
        print("-" * 46)


def ui_spacer(lines=2):
    for _ in range(lines):
        ui_print("")
