def answer_one():
    df['Country'] = df.index
    x = max(df['Gold'])
    y = df[df['Gold'] == x]
    return y['Country']


answer_one()


def answer_two():
    df['Country'] = df.index
    x = max(df['Gold'] - df['Gold.1'])
    y = df[df['Gold'] - df['Gold.1'] == x]
    return y['Country']


answer_two()

def answer_three():
    df['Country'] = df.index
    x = df[(df['Gold'] > 0) & (df['Gold.1'] > 0)]
    y = max((x['Gold'] - x['Gold.1']) / x['Gold.2'])
    z = x[((x['Gold'] - x['Gold.1']) / x['Gold.2']) == y]
    return z['Country']

answer_three()

def answer_four():
    df['Country'] = df.index
    df2 = df.reset_index()
    df2 = df2.set_index('Country')
    df2['Weighted'] = df2['Gold.2']*3 + df2['Silver.2']*3 + df2['Bronze.2']*1
    points = df2.loc[:,['Weighted']]
    return points

answer_four()

for item in census_df_stname:
    census_df_stname.loc['Alabama'].count()

    census_df_stname = census_df[['STNAME','CTYNAME']]
    census_df_stname = census_df_stname.set_index('STNAME')






for c in range (0, 51):
        cty = list_of_stname[c]
        for c in range (0, 3):
            qualquer.append(dff.iloc[c])




for c in range (0, 51):
        cty = list_of_stname[c]
        for c in range (0, 3):
            qualquer.append(dff.loc[cty])

dff.loc['California'].iloc[0]

for c in range (0, 51):
        cty = list_of_stname[c]
        print(cty)
        qualquer.append(dff.loc[cty].iloc[0])
        qualquer.append(dff.loc[cty].iloc[1])
        qualquer.append(dff.loc[cty].iloc[2])
        print(qualquer)


 or (deltaq7['delta1112'] == winner) or (deltaq7['delta1113'] == winner) or (deltaq7['delta1114'] == winner) or (deltaq7['delta1115'] == winner) or (deltaq7['delta1213'] == winner) or (deltaq7['delta1214'] == winner) or (deltaq7['delta1215'] == winner) or (deltaq7['delta1314'] == winner) or (deltaq7['delta1315'] == winner) or (deltaq7['delta1415'] == winner)]
    return x

if delta1415_pos['CTYNAME'][:9]=='Washington'