analysis_history = []

def save_report(sector, report):

    analysis_history.append({
        "sector": sector,
        "report": report
    })

def get_reports():
    return analysis_history