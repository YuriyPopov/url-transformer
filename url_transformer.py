from lark import Lark, Transformer

class UrlTransformer(Transformer):

    def start(self, branch):
        return "\n".join(branch)
    
    def url(self, branch):
        return "".join(branch)
    
    def endpoint(self, branch):
        ep = f"/{str(branch[0]).replace('-', '?x=')}"
        return f"{ep}{branch[1]}" if len(branch) == 2 else ep

    def params(self, branch):
        kv = f"&{branch[0]}={branch[1]}"
        return f"{kv}{branch[2]}" if len(branch) == 3 else kv

if __name__ == "__main__":
    
    text = """
    https://www.website.com/dir-test?key=val
    https://www.website.com/dir
    https://www.website.com/dir-test-test1/subdir-test100?key=val&key1=val1
    https://www.website.com/dir-test-test1/subdir-test100/subdir01-a-b-c?key=val&key1=val1&key99=val99
    """
    ast = Lark.open('grammar.lark',__file__).parse(text)
    # print(ast.pretty())

    result = UrlTransformer().transform(ast)
    print(result)