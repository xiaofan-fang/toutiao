from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession,async_sessionmaker

#数据库URL
ASYNC_DATABASE_URL = "mysql+aiomysql://root:123456@localhost:3306/news_app?charset=utf8mb4"

#创建异步引擎
async_engine = create_async_engine(
    ASYNC_DATABASE_URL,
    echo=True, #可选输出日志
    pool_size=10, #设置连接池中保持的持久连接数
    max_overflow=20, #设置连接池允许创建的额外连接数
    pool_timeout=10,#设置连接超时时间（默认是30秒）
    pool_recycle=3600, #连接回收时间（默认是-1，代表永不回收）
    pool_pre_ping=True, #连接前是否预检查（默认为false）
)

#创建异步会话工厂
AsyncSessionLocal = async_sessionmaker(
    bind=async_engine,#连接引擎
    class_=AsyncSession,#session类的类型
    autoflush=True,#是否在查找之前执行flush操作
    expire_on_commit=False,#是否在执行commit操作之后session就过期
)

#依赖项，用于获取数据库会话
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
        finally:
            await session.close()
