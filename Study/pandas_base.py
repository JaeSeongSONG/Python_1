# 데이터 프레임
'''
- 타입----------------------------------------------------------------------------------
    df.dtypes
    df[ 'col' ].dtype
    pd.to_datetime(df[ 'col' ], format = '%Y-%m-%d' )
    df.astype()
    pd.to_numeric( df[''] )
    
    glob.glob( './data/fhv_*' ) -> 특정 패턴의 이름을 가진 데이터를 한 번에 읽을 수 있음

- basic method----------------------------------------------------------------------------------
    df.columns
    df.index = df.keys()
    df.values = df.get_values -> series의 데이터가 있음
    df.shape
    df.shape[ 0 ] -> 전체 행의 데이터 개수 출력
    df.loc[행, 열] -> 인덱스를 기준으로 행 데이터 추출
    df.iloc[행, 열] -> 행 번호를 기준으로 행 데이터 추출
    df_1.append(df)
    df.drop( [ 'Age' ], axis = 1 )
    df.describe()
    df.duplicated([ 'col' ], keep = ( first, last, false ) ) -> boolean 타입으로 출력 
    df.drop_duplicates( [ 'col' ], keep = ( first, last, false ) )
    df.sort_values( by = ' ', ascending = True or False )
    df.sort_index( ascending = True of False )
    df.reset_index()
    df.replace( '바꿀 대상', '바꿀 것' )
    
    str.split( ' ' )

- 저장----------------------------------------------------------------------------------
    df.to_csv( './data/project.csv' )

- 그룹화한 데이터 통계----------------------------------------------------------------------------------
    df.groupby( 'year' )[ 'lifeExp' ].mean()
    -> 연도별 그룹화 후 평균

    df.groupby( 'year', 'continent' )[ 'lifeExp', 'gdpPercap' ].mean()
    -> 여러가지 변수로 그룹화 후 통계 작성도 가능

    df.groupby( 'continent' )[ 'country' ].nunique()
    -> 그룹화한 데이터의 빈도수 
    
    df.groupby( 'year' ).lifeExp.agg( my_mean )
    -> 그룹화한 데이터에 함수 적용
    
    df.groupby( 'year' ).lifeExp.transform( my_zscore )


    
- 데이터 생성하기----------------------------------------------------------------------------------
    - Series
        s = pd.Series([ 'Wes McKinney', 'Creator of Pandas' ], index = [ 'Person', 'Who' ])
    
    - DataFrame
        d = pd.DataFrame( data = { 'Occupation' : [ 'Chemist', 'Statistician' ],
                                   'Born' : [ '1920', '1876' ],
                                   'Died' : [ '1958', '1937' ],
                                   'Age' : [ 37, 61 ] },
                          index = [ 'Rosaline', 'William' ],
                          columns = [ 'Occupation', 'Born', 'Died', 'Age' ] )
                          
- 데이터 연결하기----------------------------------------------------------------------------------
    pd.concat( [ df1, df2 ] )
    
    - 행이 1개 일 때
    df1.append( df2, ignore_index = True ) <- ignore_index = 인덱스 무시하고 다시 0부터 지정
    
    - 겹치는 열을 기준으로 합칠 때 ( 공통 열만 연결 -> 내부 조인 )
    pd.concat( [ df1, df2 ], ignore_index = True, join = 'inner' )
    
    - merge
    왼쪽.merge( 오른쪽, left_on = ' ', right_on = ' ' )
    left_on -> 왼쪽 데이터에서 기준이 될 열
    right_on -> 오른쪽 데이터에서 기준이 될 열
    결국, left_on == right_on 이 되어야 함 ( 여러개의 열도 가능 )

- 누락값----------------------------------------------------------------------------------
    누락값을 사용하기 위해서는 from numpy import NaN, nan, NAN
    
    - isnull()
    - notnull()
    
    - 누락값 처리하기
        df.fillna( 0 )
        df.fillna( method = 'ffill' ) -> 누락값이 나타나기 전 값으로 되돌림
        df.fillna( method = 'bfill' ) -> 누락값이 나타난 이후의 첫 번째 값으로 앞쪽의 누락값이 모두 변경
        df.interpolate() -> 누락값 양쪽에 있는 값을 이용하여 중간값을 구해 처리
        df.dropna()
    
- 깔끔한 데이터----------------------------------------------------------------------------------
    - melt method
        지정한 열의 데이터를 모두 행으로 정리
    
        id_vars = 위치를 그대로 유지할 열의 이름 지정 
        value_vars = 행으로 위치를 변경할 열의 이름 지정
        var_name = value_vars로 위치를 변경한 열의 이름 지정
        value_name = var_name으로 위치를 변경한 열의 데이터를 저장한 열의 이름을 지정
        
        pd.melt( df, id_vars = ' ' )
        
- 문자열----------------------------------------------------------------------------------
    - method
        str.capitalize() -> 첫 문자 대문자
        str.count() -> 수 세기
        str.startswith(), endswith() -> ~로 시작하는, 끝나는
        str.find(), str.index() -> 찾을 문자열의 첫 번째 인덱스를 반환
        str.strip(), lstrip(), rstrip() -> 빈칸 제거
        str.split( '구분자' ) = str.partition()
        str.replace( 'A', 'B', count ) -> A를 count 수에 따라 B로 변경
        str.zfill( with = 숫자 ) -> 숫자만큼 칸을 만들고 빈 칸을 '0'으로 채움
        
    - JOIN method
        '구분자'.join(리스트) -> list의 문자들 사이에 구분자를 넣어 합침
        
    - SPLITLINES method
        str.splitlines() -> 여러 행을 가진 문자열을 분리한 다음 list로 반환
        
- Formating----------------------------------------------------------------------------------
    %d % 10
    f-strings -> f'i am a {}'
    
- 정규식----------------------------------------------------------------------------------
    공부필요

- 함수----------------------------------------------------------------------------------
    def my_sq(x):
        return x ** 2
        
    def my_exp(2, 4):
        return x ** n
        
    - apply method ( df = Series )
        df[ 'a' ].apply( my_sq )
        
        df[ 'a' ].apply( my_exp, n = 2 )
        
    - apply method ( df = DataFrame )
        다른 인자를 지정해주거나 정의
        df.apply( my_sq, axis = 0 )
        
        
        
        
'''      