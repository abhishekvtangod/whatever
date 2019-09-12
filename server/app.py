import falcon
import pandas as pd


def check():
    data_frame = pd.read_csv("raw_final.csv")
    print(data_frame)


check()

# class QuoteResource:
#     def on_get(self, req, resp):
#         """Handles GET requests"""
#         quote = {
#         }

#         resp.media = quote


# api = falcon.API()
# api.add_route('/quote', QuoteResource())
