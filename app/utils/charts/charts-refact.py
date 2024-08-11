import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

class Charts:
    def __init__(self):
        self.init = 0

    @staticmethod
    def format_currency_column(df, column, currency='R$'):
        return df[column].map(f'{currency}{{:,.2f}}'.format)
    
    @staticmethod
    def create_table(df):
        header = ["Date"] + list(df.columns)
        cells = [df.index.strftime("%d/%m/%Y")] + [df[col] for col in df.columns]

        return go.Table(
            header=dict(
                values=header,
                fill_color='paleturquoise',
                align="left"
            ),
            cells=dict(
                values=cells,
                fill_color='lavender',
                align="left"
            )
        )

    @staticmethod
    def table_dataframe_to_jpeg(ticker, df):
        df["open"] = Charts.format_currency_column(df, "open")
        df["high"] = Charts.format_currency_column(df, "high")
        df["low"] = Charts.format_currency_column(df, "low")
        df["close"] = Charts.format_currency_column(df, "close")

        fig = go.Figure(data=[Charts.create_table(df)])
        fig.update_layout(height=1200, width=1200, title_text=ticker)
        fig.write_image(f"app/charts/jpeg/{ticker}.jpeg")

    @staticmethod
    def add_scatter_trace(fig, df, row, col, y_column, trace_name, color, mode='lines+markers', additional_kwargs=None):
        additional_kwargs = additional_kwargs or {}
        fig.add_trace(
            go.Scatter(
                x=df.index, y=df[y_column],
                mode=mode, name=trace_name,
                line=dict(color=color, width=1),
                **additional_kwargs
            ),
            row=row, col=col
        )

    @staticmethod
    def candlestick_chart(ticker, df, extension_type):
        df["open"] = Charts.format_currency_column(df, "open")
        df["high"] = Charts.format_currency_column(df, "high")
        df["low"] = Charts.format_currency_column(df, "low")
        df["close"] = Charts.format_currency_column(df, "close")

        fig = make_subplots(
            rows=4, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.05,
            specs=[[{"type": "table"}],
                   [{"type": "scatter"}],
                   [{"type": "scatter"}],
                   [{"type": "scatter"}]]
        )

        fig.add_trace(Charts.create_table(df), row=1, col=1)

        Charts.add_scatter_trace(fig, df, row=2, col=1, y_column='macdh', trace_name='MACDH', color='blue')
        Charts.add_scatter_trace(fig, df, row=2, col=1, y_column='macdh', trace_name='R+ (buy)', color='green',
                                 mode='markers', additional_kwargs={'marker': dict(symbol='triangle-up')})
        Charts.add_scatter_trace(fig, df, row=2, col=1, y_column='macdh', trace_name='R- (sell)', color='red',
                                 mode='markers', additional_kwargs={'marker': dict(symbol='triangle-down')})

        Charts.add_scatter_trace(fig, df, row=3, col=1, y_column='close', trace_name='Price (close)', color='green')
        Charts.add_scatter_trace(fig, df, row=4, col=1, y_column='volume', trace_name='Volume', color='grey')

        fig.update_xaxes(
            rangeslider=dict(visible=False),
            rangeselector=dict(
                buttons=[
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all")
                ]
            )
        )

        fig.update_layout(height=1200, width=1200, title_text=ticker)

        if extension_type == "html":
            filename = f"charts/html/{ticker}.html"
            fig.write_html(filename)
        elif extension_type == "jpeg":
            filename = f"charts/jpeg/{ticker}.jpeg"
            fig.write_image(filename)
        else:
            fig.show()
            filename = None

        return filename