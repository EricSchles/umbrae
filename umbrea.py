import statistics as st

def umbrea(data, forecast):
    """
    Unscaled Mean Bounded Relative Absolute Error
    Formula taken from:
    https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5365136/
    @data - Y[i]
    @forecast - F[i]
    """
    numerator = [abs(datum - forecast[idx]) for idx, datum in enumerate(data)]
    series_one = data[1:]
    series_two = data[:-1]
    denominator = [abs(elem - series_two[idx]) for idx, elem in enumerate(series_one)]
    final_series = [numerator[idx]/(numerator[idx] + denominator[idx])
                    for idx in range(len(numerator))]
    mbrae = st.mean(final_series)
    return mbrea/(1-mbrea)
