from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
import os

def generate_report(results, plot_file='plot.png'):
    try:
        c = canvas.Canvas("report.pdf", pagesize=letter)
        c.drawString(100, 750, "EvoQEC Pro Heavy Report")
        c.drawString(100, 700, f"d={results['d']}, LER={results['LER']:.2e}, QuTiP Fid={results['QuTiP Fid']:.3f}")
        c.drawImage(plot_file, 100, 400, 400, 300)
        c.save()
        return "report.pdf"
    except Exception as e:
        print(f"Report error: {e}")
        return None

def license_check(key='EVOQEC2025'):
    try:
        return input("Pro Key: ") == key
    except:
        return False

def tutorial_gen(results):
    try:
        tut = f"# EvoQEC Heavy Tutorial\nQiskit Synd: {results['Qiskit Synd']:.3f}\nStim LER: {results['Stim LER']:.3f}\n# 2025 Updates: Qiskit 1.0+ MWPM"
        with open('tutorial.md', 'w') as f: f.write(tut)
        return 'tutorial.md'
    except Exception as e:
        print(f"Tut error: {e}")
        return None