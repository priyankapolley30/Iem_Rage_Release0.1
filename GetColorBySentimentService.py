class GetColorBySentimentService:

    def get_color_by_sentiment(self, sentiment):
        if (sentiment == "Neutral"):
            return "#9CC0E7"
        elif (sentiment == "Positive"):
            return "#39ff14"
        else:
            return "#ff073a"