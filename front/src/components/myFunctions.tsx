export function doesExist(_var: string, table: string[]): boolean {
    for (const t of table) {
      if (t === _var){
        return true;
      }
    }
    return false;
  }
