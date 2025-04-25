class Solution:
    def displayTable(self, orders: list[list[str]]) -> list[list[str]]:
        """
        Create a display table from restaurant orders.
        
        Args:
            orders: A list of orders where each order is [customerName, tableNumber, foodItem].
            
        Returns:
            A "display table" where the first row is the header with "Table" followed by food items
            in alphabetical order, and each subsequent row shows how many of each food item each
            table ordered, with tables sorted in numerically increasing order.
        """
        foods = set()
        tables = set()
        
        for _, table, food in orders:
            foods.add(food)
            tables.add(table)

        food_list = sorted(list(foods))

        table_list = sorted(list(tables), key=int)

        result = [["Table"] + food_list]

        table_orders = {}
        for _, table, food in orders:
            if table not in table_orders:
                table_orders[table] = {}
            
            if food not in table_orders[table]:
                table_orders[table][food] = 0
            
            table_orders[table][food] += 1
        
        for table in table_list:
            row = [table]
            
            for food in food_list:
                count = table_orders.get(table, {}).get(food, 0)
                row.append(str(count))
            
            result.append(row)
        
        return result
    