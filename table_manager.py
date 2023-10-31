import pandas as pd


def get_merged(df_conv, df_stats, stat="mean"):
    df_stats = df_stats[["Alias","Type", "h_{}".format(stat), "r_{}".format(stat), "dmax_{}".format(stat)]].copy()
    df_aux = df_conv[["Id_HQ", "Alias_HQ", "Alias_MBC7", "Type_MBC7"]].copy()
    df_aux = pd.merge(left=df_aux, right=df_stats, left_on="Alias_MBC7", right_on="Alias", how="left")

    df_nat = df_stats.query("Type == 'Natural cover'").copy()
    df_ex = df_stats.query("Type == 'Extensive use'").copy()
    df_in = df_stats.query("Type == 'Intensive use'").copy()
    # fill Nf values
    df_aux.loc[df_aux['Alias_MBC7'] == "Nf", "h_{}".format(stat)] = df_nat["h_{}".format(stat)].mean()
    df_aux.loc[df_aux['Alias_MBC7'] == "Nf", "r_{}".format(stat)] = df_nat["r_{}".format(stat)].mean()
    df_aux.loc[df_aux['Alias_MBC7'] == "Nf", "dmax_{}".format(stat)] = df_nat["dmax_{}".format(stat)].mean()
    # fill Nv values
    df_aux.loc[df_aux['Alias_MBC7'] == "Nv", "h_{}".format(stat)] = df_ex["h_{}".format(stat)].mean()
    df_aux.loc[df_aux['Alias_MBC7'] == "Nv", "r_{}".format(stat)] = df_ex["r_{}".format(stat)].mean()
    df_aux.loc[df_aux['Alias_MBC7'] == "Nv", "dmax_{}".format(stat)] = df_ex["dmax_{}".format(stat)].mean()
    # fill No values
    df_aux.loc[df_aux['Alias_MBC7'] == "No", "h_{}".format(stat)] = 0
    df_aux.loc[df_aux['Alias_MBC7'] == "No", "r_{}".format(stat)] = 0
    df_aux.loc[df_aux['Alias_MBC7'] == "No", "dmax_{}".format(stat)] = 0
    # fill Na values
    df_aux.loc[df_aux['Alias_MBC7'] == "Na", "h_{}".format(stat)] = 0
    df_aux.loc[df_aux['Alias_MBC7'] == "Na", "r_{}".format(stat)] = 0
    df_aux.loc[df_aux['Alias_MBC7'] == "Na", "dmax_{}".format(stat)] = 0
    return df_aux

def get_threat_table(df_conv, df_stats, stat="mean"):
    df_merged = get_merged(df_conv=df_conv, df_stats=df_stats, stat=stat)
    df_stats = df_merged.query("Type_MBC7 == 'Intensive use' or Type_MBC7 == 'Extensive use'")
    df_threats = pd.DataFrame(
        {
            "THREAT": df_stats["Alias_HQ"].str.upper(),
            "MAX_DIST": df_stats["dmax_{}".format(stat)].values,
            "WEIGHT": df_stats["r_{}".format(stat)].values,
            "DECAY": ["linear" for i in range(len(df_stats))],
            "BASE_PATH": ["" for i in range(len(df_stats))],
            "CUR_PATH": ["{}.tif".format(df_stats["Alias_HQ"].values[i].upper()) for i in range(len(df_stats))],
            "FUT_PATH": ["" for i in range(len(df_stats))]
        }
    )
    return df_threats.round(3)

def get_lulc_table(df_conv, df_stats, stat="mean"):
    df_merged = get_merged(df_conv=df_conv, df_stats=df_stats, stat=stat)
    df_threats = get_threat_table(df_conv=df_conv, df_stats=df_stats, stat=stat)
    df_lulc = pd.DataFrame(
        {
            "LULC": df_merged["Id_HQ"].values,
            "NAME": df_merged["Alias_HQ"].str.upper(),
            "HABITAT": df_merged["h_{}".format(stat)].values
        }
    )
    for i in range(len(df_threats)):
        t = df_threats["THREAT"].values[i]
        r = df_threats["WEIGHT"].values[i]
        # ----------- apply formula ----------
        df_lulc[t.upper()] = ((0.9 * (r* (1 - df_lulc["HABITAT"].values))) + 0.1)
        # set zero No and Na
        df_lulc[t.upper()].values[-1] = 0
        df_lulc[t.upper()].values[-2] = 0
    return df_lulc.round(3)

if __name__ == '__main__':
    df_stats = pd.read_csv("./responses_forms/stats_table.csv", sep=";")
    df_conv = pd.read_csv("./lulc_conversion_table.csv", sep=",")

    lst_stats = ["p05", "mean", "p95"]
    for s in lst_stats:
        df_t = get_threat_table(df_conv=df_conv, df_stats=df_stats, stat=s)
        df_lulc = get_lulc_table(df_conv=df_conv, df_stats=df_stats, stat=s)
        df_t.to_csv("./threat_{}.csv".format(s), sep=",", index=False)
        df_lulc.to_csv("./lulc_{}.csv".format(s), sep=",", index=False)