import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

class Charts:
    def __init__(self):
        self.init = 0

    def table_dataframe_to_jpeg(ticker, df):
        header = list(df.columns)
        header.insert(0, "Date")

        fig = go.Figure(data=[go.Table(
            header=dict(
                values=header,
                fill_color='paleturquoise',
                align="left"
            ),
            cells=dict(
                values=[df.index.strftime("%d/%m/%Y"), df["open"].map('${:,.2f}'.format), 
                    df["high"].map('R${:,.2f}'.format), df["low"].map('R${:,.2f}'.format), 
                    df["close"].map('R${:,.2f}'.format), df["volume"], 
                    df["macd"].map('{:,.3f}'.format), df["macds"].map('{:,.3f}'.format), 
                    df["macdh"].map('{:,.3f}'.format), df["macdh_a"]],
                fill_color='lavender',
                align = "left"),
        )])

        fig.update_layout(height=1200, width=1200, title_text=ticker)

        fig.write_image("app/charts/jpeg/{}.jpeg".format(ticker))

    def candlestick_chart(ticker, df, extension_type):

        header = list(df.columns)
        header.insert(0, "Date")

        fig = make_subplots(
            rows=4, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.05,
            specs=[[{"type": "table"}],
                [{"type": "scatter"}],
                [{"type": "scatter"}],
                [{"type": "scatter"}]]
        )

        headerColor = 'grey'
        rowEvenColor = 'lightgrey'
        rowOddColor = 'white'

        fig.add_trace(go.Table(
            header=dict(
                values=header,
                align="left",
                line_color='darkslategray',
                fill_color=headerColor,
                font=dict(color='white', size=12)
            ),
            cells=dict(
                values=[df.index.strftime("%d/%m/%Y"), df["open"].map('${:,.2f}'.format), 
                    df["high"].map('R${:,.2f}'.format), df["low"].map('R${:,.2f}'.format), 
                    df["close"].map('R${:,.2f}'.format), df["volume"], 
                    df["macd"].map('{:,.3f}'.format), df["macds"].map('{:,.3f}'.format), 
                    df["macdh"].map('{:,.3f}'.format), df["macdh_a"]],
                fill_color = [[rowOddColor,rowEvenColor,rowOddColor, rowEvenColor,rowOddColor]*5],
                font = dict(color = 'black', size = 12),
                align = "left")
        ), row=1, col=1)

        fig.append_trace(go.Scatter(
            x=df.index, y=df['macdh'],
            mode='lines+markers', name='macdh',
            line=dict(color='blue', width=1)
        ), row=2, col=1)

        fig.append_trace(go.Scatter(
            x=df.index, y=df['macdh'].where(df['macdh_a']=='R+')-0.03, mode='markers', marker_size=10,
            marker=dict(symbol='triangle-up'), name='R+ (buy)', marker_color='green'
        ), row=2, col=1)

        fig.append_trace(go.Scatter(
            x=df.index, y=df['macdh'].where(df['macdh_a']=='R-')-0.03, mode='markers', marker_size=10,
            marker=dict(symbol='triangle-down'), name='R- (sell)', marker_color='red'
        ), row=2, col=1)

        """fig.append_trace(go.Scatter(
            x=df.index, y=df['macd'],
            mode='lines+markers', name='macd',
            line=dict(color='red', width=1)
        ), row=2, col=1)

        fig.append_trace(go.Scatter(
            x=df.index, y=df['macds'],
            mode='lines+markers', name='macds',
            line=dict(color='orange', width=1)
        ), row=2, col=1)"""

        fig.append_trace(go.Scatter(
            x=df.index, y=df['close'],
            mode='lines+markers', name='price (close)',
            line=dict(color='green', width=1)
        ), row=3, col=1)

        fig.append_trace(go.Scatter(
            x=df.index, y=df['volume'],
            mode='lines+markers', name='volume',
            line=dict(color='grey', width=1)
        ), row=4, col=1)

        fig.update_xaxes(
            rangeslider=dict(visible=False),
            rangeselector=dict(
                buttons=list([
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ])
            )
        )

        fig.update_layout(height=1200, width=1200, title_text=ticker)

        if extension_type == "html":
            filename = "app/charts/html/{0}.html".format(ticker)
            fig.write_html(filename)

            return filename

        elif extension_type == "jpeg":
            filename = "app/charts/jpeg/{0}.jpeg".format(ticker)
            fig.write_image(filename)

            return filename
        else:
            fig.show()
            return None

